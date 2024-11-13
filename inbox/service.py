def get_path_for_image_message(instance, filename):
    return f"message/inbox/{instance.inbox.id}/{filename}"
