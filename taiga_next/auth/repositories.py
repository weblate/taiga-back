from .models import User


def get_user_by_username_or_email(username_or_email: str, extra_filters: dict = {}) ->  Union[User, None]:
    qs = User.objects.filter(Q(username__iexact=username_or_email) |
                             Q(email__iexact=username_or_email),
                             **extra_filters)

    if len(qs) > 1:
        # NOTE: This is because Taiga was case sensitive for email and
        #       username in the pass
        qs = qs.filter(Q(username=username_or_email) |
                       Q(email=username_or_email))

    if len(qs) == 0:
        return None

    return  qs[0]
