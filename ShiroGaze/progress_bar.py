from progress.bar import Bar


class ProgressBar(Bar):
    message = "Веду поиск"
    suffix_base = "(%(index)d / %(max)d) | {site}"
