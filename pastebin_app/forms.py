from django import forms
FAVORITE_COLORS_CHOICES = [
    ('plaintext', 'Plain Text'),
    ('html', 'Html'),
    ('css', 'Css'),
    ('javascript', 'Javascript'),
    ('python', 'Python'),
    ('php', 'Php'),
    ('java', 'Java'),
]

class PasteForm(forms.Form):
    title = forms.CharField(max_length=30)
    paste_text = forms.CharField(
        widget=forms.Textarea, help_text="Enter Paste Here!")
    p_language = forms.CharField(
        widget=forms.Select(choices = FAVORITE_COLORS_CHOICES), help_text="Select Language", required=False)
    user = forms.CharField(max_length=10)

class CommentForm(forms.Form):
    Name = forms.CharField(max_length=10, required=True)
    comment = forms.CharField(widget=forms.Textarea, help_text="Your comment Here!", required=True)
    