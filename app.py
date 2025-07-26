import os
from flask import Flask, render_template

# 初始化 Flask 应用
app = Flask(__name__)

# 根路由 - 首页
@app.route('/')
def home():
    # 可传递变量到模板
    return render_template('home.html', title="首页", message="祝表姐表姐夫新婚快乐！")

# 测试路由
@app.route('/about')
def about():
    return render_template('about.html', title="关于", content="这是一个部署在 Vercel 上的 Flask 应用")

# 启动配置 - 适配 Vercel 环境
if __name__ == '__main__':
    # 从环境变量获取端口（Vercel 会自动设置），默认 5000
    port = int(os.environ.get('PORT', 5000))
    # 绑定 0.0.0.0 允许外部访问
    app.run(host='0.0.0.0', port=port)
