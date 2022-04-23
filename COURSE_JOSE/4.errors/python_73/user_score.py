from signal import raise_signal


class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    def __repr__(self) -> str:
        return f'<User {self.name}>'

    
def get_user_score(user):
    try:
        return perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values were provided to our calculation function')
    else:
        if user.score > 500:
            send_engagement_notification(user)


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification was sent to the user {user} successfully!')


my_user = User('Rolf', {'click': 61, 'hits': 100})
get_user_score(my_user)
