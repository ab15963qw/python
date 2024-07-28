from flask import Flask, render_template, request, jsonify
import twstock
import matplotlib.pyplot as plt
import io
import base64
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stock', methods=['POST'])
def stock():
    stock_id = request.form['stock_id']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    
    # 将字符串转换为日期对象
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    stock = twstock.Stock(stock_id)
    data = stock.fetch_from(start_date.year, start_date.month)

    # 过滤数据，只保留在指定日期范围内的数据
    filtered_data = [d for d in data if start_date <= d.date <= end_date]
    
    dates = [d.date for d in filtered_data]
    prices = [d.close for d in filtered_data]

    # 使用 BestFourPoint 获取买入和卖出信号
    best_four_point = twstock.BestFourPoint(stock)
    buy_signals = [i for i in range(len(dates)) if best_four_point.best_four_point()[0]]
    sell_signals = [i for i in range(len(dates)) if best_four_point.best_four_point()[1]]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, label='Price', marker='o')

    # 标记买入信号
    for i in buy_signals:
        plt.scatter(dates[i], prices[i], color='green', label='Buy', marker='^', alpha=1)

    # 标记卖出信号
    for i in sell_signals:
        plt.scatter(dates[i], prices[i], color='red', label='Sell', marker='v', alpha=1)

    # 在图表中显示每个日期的价格
    for i, txt in enumerate(prices):
        plt.annotate(txt, (dates[i], prices[i]), textcoords="offset points", xytext=(0,5), ha='center')

    plt.legend(loc='best', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Stock Price and Buy/Sell Signals for {stock_id}')
    
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # 获取实时股票信息
    realtime_stock = twstock.realtime.get(stock_id)
    if realtime_stock['success']:
        real_time_price = realtime_stock['realtime']['latest_trade_price']
        high = realtime_stock['realtime']['high']
        low = realtime_stock['realtime']['low']
        volume = realtime_stock['realtime']['accumulate_trade_volume']
    else:
        real_time_price = 'N/A'
        high = 'N/A'
        low = 'N/A'
        volume = 'N/A'

    return render_template('stock.html', plot_url=plot_url, stock_id=stock_id,
                           real_time_price=real_time_price, high=high, low=low, volume=volume)

@app.route('/realtime_stock/<stock_id>')
def realtime_stock(stock_id):
    # 获取实时股票信息
    realtime_stock = twstock.realtime.get(stock_id)
    if realtime_stock['success']:
        real_time_price = realtime_stock['realtime']['latest_trade_price']
        high = realtime_stock['realtime']['high']
        low = realtime_stock['realtime']['low']
        volume = realtime_stock['realtime']['accumulate_trade_volume']
    else:
        real_time_price = 'N/A'
        high = 'N/A'
        low = 'N/A'
        volume = 'N/A'

    return jsonify({
        'real_time_price': real_time_price,
        'high': high,
        'low': low,
        'volume': volume
    })

if __name__ == '__main__':
    app.run(debug=True)
