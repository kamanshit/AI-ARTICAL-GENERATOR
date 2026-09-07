from django import forms

class ArticleForm(forms.Form):
    topic = forms.CharField(
        max_length=200,
        label="Article Topic",
        required=True
    )

    def clean_topic(self):
        topic = self.cleaned_data["topic"]

        if len(topic.strip())<=3:
            raise forms.ValidationError(
                "Topic must contain more than 3 characters"
            )

        return topic.strip()