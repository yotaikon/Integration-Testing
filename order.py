class NotificationService:
    def send_email(self, user_email, message):
        # 实际发送邮件的复杂逻辑 ...
        print(f"Email sent to {user_email}")
        return True


class OrderService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def place_order(self, user_email, order_details):
        # ...处理订单逻辑 ...
        print("Order placed successfully.")
        # 下单成功后发送邮件
        self.notification_service.send_email(
            user_email,
            "Your order was successful!"
        )
        return True
