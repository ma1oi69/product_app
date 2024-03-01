from product.models import UserProduct, Group, UserGroup


def add_access(product_id, user_id):
    UserProduct.objects.create(product_id=product_id, user_id=user_id)


def create_group(count_groups, product):
    for _ in range(1, int(count_groups)):
        name_group = f"{product.name}{Group.objects.count()}"
        Group.objects.create(name=name_group, min_students=product.min_students,
                             max_students=product.max_students,
                             product_id=product.id)


# def add_student_to_group():
#     UserGroup.objects.create()
