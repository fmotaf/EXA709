import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import random

# 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r',
# 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges',
# 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r',
# 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r',
# 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r',
# 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r',
# 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r',
# 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r',
# 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray',
# 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r',
# 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r',
# 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r',
# 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r',
# 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r',
# 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r',
# 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

COLOR_TYPE_MIXED = "tab20b"
COLOR_TYPE_MIXED2 = "tab20_r"
COLOR_TYPE_BLUE = "Blues"
COLOR_TYPE_GREEN = "Greens"
COLOR_TYPE_RED = "Reds"
COLOR_TYPE_COPER = "copper"
COLOR_TYPE_BONE = "bone"
COLOR_TYPE_PUBUGN = "PuBuGn"
COLOR_TYPE_YLORBR = "YlOrBr"
COLOR_TYPE_YLORRD = "YlOrRd"
COLOR_TYPE_RDYLBU = "RdYlBu"
COLOR_TYPE_PASTEL = "Pastel1"
COLOR_TYPE_BUGN = "BuGn"
COLOR_TYPE_RAINBOW = "rainbow"


def chart_header(data, legend, color_type):
    data = data.copy()
    max_value = max(list(data.values()))

    if legend != None:
        legends_keys = list(legend.keys())

    colors = plt.get_cmap(color_type)(np.linspace(0.2, 0.8, len(data.keys())))

    new_data = []
    handlers = []
    for index in range(len(data.keys())):
        if legend != None:
            legend_key = legends_keys[index]
            label = legend[legend_key]
            new_data.append(data.get(legend_key))
            handlers.append(mpatches.Patch(color=colors[index], label=label))
        else:
            new_data.append(data.popitem())
            handlers.append(mpatches.Patch(color=colors[index]))

    return (new_data, handlers, colors, max_value)


def pie(
    title: str,
    data: dict,
    legend=None,
    legend_title=None,
    y_label=None,
    x_label=None,
    color_type=COLOR_TYPE_BLUE,
):
    (new_data, handlers, colors, _) = chart_header(data, legend, color_type)


    def absolute_value(value):
        sizes = np.array([item for item in data.values()])
        return np.round(value / 100.0 * sizes.sum(), 0)

    fig, ax = plt.subplots()
    ax.pie(
        x=new_data,
        colors=colors,
        radius=3,
        center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"},
        autopct=absolute_value,
        frame=True,
    )

    ax.set_title(title)

    if y_label:
        ax.set_ylabel(y_label)

    if x_label:
        ax.set_xlabel(x_label)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

    """ ax.set(
        xlim=(0, 1),
        xticks=np.arange(1, len(new_data) + 2),
        ylim=(0, len(new_data) + 1),
        yticks=np.arange(1, len(new_data) + 1),
    ) """

    ax.legend(handles=handlers, title=legend_title)

    plt.subplots_adjust(
        left=0.1 if y_label else 0.08,
        bottom=0.12 if x_label else 0.06,
        right=0.94,
        top=0.94,
    )

    plt.show()


def bar(
    title: str,
    data: dict,
    legend: list = None,
    legend_title=None,
    x_label=None,
    x_label_item=None,
    y_label=None,
    color_type=COLOR_TYPE_BLUE,
):
    (new_data, handlers, colors, max_value) = chart_header(data, legend, color_type)

    if type(x_label_item) == str:
        x_label_item = ["%d%s" % (i, x_label_item) for i in range(len(new_data))]

    x = x_label_item if x_label_item else 0.5 + np.arange(len(new_data))
    y = data.values()

    fig, ax = plt.subplots()
    ax.bar(
        x,
        y,
        width=0.7,
        edgecolor="white",
        linewidth=1,
        color=colors,
    )
    ax.set_title(title)

    if y_label:
        ax.set_ylabel(y_label)

    if x_label:
        ax.set_xlabel(x_label)

    ax.set(
        xlim=(0, 1),
        xticks=np.arange(1, len(new_data) + 1),
        ylim=(0, max_value + 2),
        yticks=np.arange(1, max_value + 2),
    )

    if legend:
        ax.legend(handles=handlers, title=legend_title)

    plt.subplots_adjust(
        left=0.1 if y_label else 0.08,
        bottom=0.12 if x_label else 0.06,
        right=0.94,
        top=0.94,
    )
    plt.show()
