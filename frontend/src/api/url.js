let baseUrl = ""; //这里是一个默认的url，可以没有
switch (process.env.NODE_ENV) {
  case 'development':
    baseUrl="http://127.0.0.1:8000/"//测试用
    break
  case 'test': // 注意这里的名字要和步骤二中设置的环境名字对应起来
    baseUrl="http://127.0.0.1:8000/"//测试用
    break
  case 'production':
    baseUrl="http://127.0.0.1:8000/"//测试用
    break
}

export default baseUrl;
