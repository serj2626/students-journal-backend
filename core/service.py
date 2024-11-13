def get_path_for_avatar(instance, filename):
    return f"{instance.user.get_user_type_display()}/avatar/{instance.user.username}/{filename}"
