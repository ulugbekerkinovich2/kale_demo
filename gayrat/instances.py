import os


def get_shots_path(instance, filename):
    return os.path.join('shots',
                        "product_%s" % str(instance.product.id),
                        filename)
