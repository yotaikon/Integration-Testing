import unittest
from unittest.mock import Mock, patch
from order import OrderService, NotificationService


class TestOrderServiceIntegration(unittest.TestCase):
    """OrderService集成测试类"""
    
    def setUp(self):
        """测试前的设置，创建模拟的NotificationService"""
        self.mock_notification_service = Mock(spec=NotificationService)
        self.order_service = OrderService(self.mock_notification_service)
    
    def test_place_order_should_send_email_notification_on_success(self):
        """测试下单成功后应该发送邮件通知"""
        # 准备测试数据
        user_email = "test@example.com"
        order_details = {"product": "测试产品", "quantity": 1}
        
        # 执行测试
        result = self.order_service.place_order(user_email, order_details)
        
        # 验证结果
        self.assertTrue(result)
        # 验证send_email方法被调用了一次
        self.mock_notification_service.send_email.assert_called_once()
        # 验证send_email方法被调用时的参数
        self.mock_notification_service.send_email.assert_called_with(
            user_email, 
            "Your order was successful!"
        )
    
    def test_place_order_should_call_send_email_with_correct_parameters(self):
        """测试下单时应该使用正确的参数调用send_email方法"""
        user_email = "customer@company.com"
        order_details = {"item": "笔记本电脑", "price": 5000}
        
        self.order_service.place_order(user_email, order_details)
        
        # 验证send_email被调用的参数完全匹配
        expected_call = unittest.mock.call(user_email, "Your order was successful!")
        self.mock_notification_service.send_email.assert_called_with(*expected_call.args)
    
    def test_place_order_should_return_true_on_success(self):
        """测试下单成功时应该返回True"""
        user_email = "user@test.com"
        order_details = {"product": "测试商品"}
        
        result = self.order_service.place_order(user_email, order_details)
        
        self.assertTrue(result)
    
    def test_place_order_should_handle_empty_order_details(self):
        """测试下单时应该能够处理空的订单详情"""
        user_email = "test@example.com"
        order_details = {}
        
        result = self.order_service.place_order(user_email, order_details)
        
        self.assertTrue(result)
        self.mock_notification_service.send_email.assert_called_once()
    
    def test_place_order_should_work_with_different_email_formats(self):
        """测试下单时应该能够处理不同格式的邮箱地址"""
        test_emails = [
            "simple@test.com",
            "user.name@domain.co.uk",
            "test+tag@example.org"
        ]
        
        for email in test_emails:
            with self.subTest(email=email):
                self.mock_notification_service.reset_mock()
                result = self.order_service.place_order(email, {"product": "测试"})
                
                self.assertTrue(result)
                self.mock_notification_service.send_email.assert_called_once_with(
                    email, 
                    "Your order was successful!"
                )


if __name__ == '__main__':
    unittest.main()
