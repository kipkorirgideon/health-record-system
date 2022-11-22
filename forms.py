import datetime
import django.forms


class FromMixin:
    required_fields = []
    labels = []
    placeholders = []
    exclude_fields = []
    initials = []
    addon_before = []
    addon_after = []
    readonly = []
    fields = []
    date_fields = []
    datetime_fields = []

    def get_placeholders(self):
        return self.placeholders

    def get_excluded_fields(self):
        return self.exclude_fields

    def get_required_fields(self):
        return self.required_fields

    def get_labels(self):
        return self.labels

    def get_initials(self):
        return self.initials

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = self.get_required_fields()
        placeholders = self.get_placeholders() or []
        labels = self.get_labels()
        initials = self.get_initials()
        fieldKeys = list(self.fields.keys())
        for field in fieldKeys:
            self.fields[field].required = bool(field in required_fields)
            self.fields[field].widget.is_required = bool(field in required_fields)

            if field in labels:
                self.fields[field].label = labels[field]
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            if field in self.addon_before:
                self.fields[field].addon_before = self.addon_before[field]
                self.fields[field].widget.attrs['addon_before'] = self.addon_before[field]
            if field in self.addon_after:
                self.fields[field].addon_after = self.addon_after[field]
                self.fields[field].widget.attrs['addon_after'] = self.addon_after[field]
            if field in initials:
                self.fields[field].initial = initials[field]

            if field in self.date_fields:
                self.fields[field].widget.attrs['data-date'] = True

            if field in self.datetime_fields:
                self.fields[field].widget.attrs['data-datetime'] = True

            if isinstance(self.fields[field], django.forms.fields.DateField):
                this_year = datetime.date.today().year
                if field == 'date_of_birth':
                    years = range(this_year - 99, this_year + 1)
                    self.fields[field].widget = SelectDateCustomWidget(years=years)


class SelectDateCustomWidget(django.forms.widgets.SelectDateWidget):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["subwidgets"][0], context["widget"]["subwidgets"][1] = context["widget"]["subwidgets"][1], \
                                                                                 context["widget"]["subwidgets"][0]
        return context
