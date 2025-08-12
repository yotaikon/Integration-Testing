# 订单系统 (Order System)

一个简单的订单管理系统，包含订单处理和邮件通知功能。

## 项目概述

本项目实现了一个基本的订单服务系统，主要功能包括：
- 订单处理服务 (`OrderService`)
- 邮件通知服务 (`NotificationService`)
- 完整的集成测试覆盖

## 项目结构

```
集成测试/
├── order.py              # 核心业务逻辑
├── test_order.py         # 集成测试文件
└── README.md            # 项目说明文档
```

## 核心组件

### NotificationService
邮件通知服务类，负责发送邮件通知。

**主要方法：**
- `send_email(user_email, message)` - 发送邮件到指定用户

### OrderService
订单服务类，处理订单业务逻辑并发送通知。

**主要方法：**
- `place_order(user_email, order_details)` - 处理订单并发送确认邮件

## 安装和运行

### 环境要求
- Python 3.6+
- 标准库（无需额外依赖）

## 测试用例概览

```
1.test_place_order_should_send_email_notification_on_success - 测试下单成功后应该发送邮件通知
2.test_place_order_should_call_send_email_with_correct_parameters - 测试下单时应该使用正确的参数调用send_email方法
3.test_place_order_should_return_true_on_success - 测试下单成功时应该返回True
4.test_place_order_should_handle_empty_order_details - 测试下单时应该能够处理空的订单详情
5.test_place_order_should_work_with_different_email_formats - 测试下单时应该能够处理不同格式的邮箱地址
```

## 测试设计特点

```
·使用Mock对象：通过Mock(spec=NotificationService)创建模拟的NotificationService
·验证方法调用：使用assert_called_once()和assert_called_with()验证send_email方法被正确调用
·清晰的测试名称：每个测试方法名都清楚地表达了测试意图
·完整的断言：验证返回值、方法调用次数和参数
·边界情况测试：包含空订单详情和不同邮箱格式的测试
```

### 运行测试
```bash
# 运行所有测试
python test_order.py

# 使用unittest模块运行
python -m unittest test_order.py

# 运行特定测试类
python -m unittest test_order.TestOrderServiceIntegration
```

## 测试覆盖

项目包含完整的集成测试，测试用例包括：

1. **`test_place_order_should_send_email_notification_on_success`** - 验证下单成功后发送邮件通知
2. **`test_place_order_should_call_send_email_with_correct_parameters`** - 验证邮件发送参数正确性
3. **`test_place_order_should_return_true_on_success`** - 验证下单成功返回值
4. **`test_place_order_should_handle_empty_order_details`** - 验证空订单详情处理
5. **`test_place_order_should_work_with_different_email_formats`** - 验证不同邮箱格式支持

## 设计模式

- **依赖注入 (Dependency Injection)**: OrderService通过构造函数接收NotificationService实例
- **模拟测试 (Mock Testing)**: 使用unittest.mock模拟外部依赖，确保测试的隔离性

## 使用示例

```python
from order import OrderService, NotificationService

# 创建通知服务实例
notification_service = NotificationService()

# 创建订单服务实例
order_service = OrderService(notification_service)

# 下单
order_details = {"product": "笔记本电脑", "quantity": 1}
result = order_service.place_order("user@example.com", order_details)

if result:
    print("订单创建成功！")
```

## 扩展建议

- 添加数据库持久化
- 实现订单状态管理
- 增加支付集成
- 添加用户认证和授权
- 实现订单历史查询
- 添加库存管理功能

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用MIT许可证。
