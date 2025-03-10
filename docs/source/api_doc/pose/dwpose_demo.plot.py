from imgutils.pose import dwpose_estimate, op18_visualize
from plot import image_plot


def _detect(img, **kwargs):
    return op18_visualize(img, dwpose_estimate(img), **kwargs)


if __name__ == '__main__':
    image_plot(
        (_detect('dwpose/lie.jpg'), 'lie'),
        (_detect('dwpose/squat.jpg'), 'squat'),
        (_detect('dwpose/halfbody.png'), 'halfbody'),
        (_detect('dwpose/2girls.png'), 'multiple'),
        columns=2,
        figsize=(9, 9),
        autocensor=False,
    )
