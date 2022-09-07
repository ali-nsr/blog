from django import forms

class CreateContactForm(forms.Form):
	full_name = forms.CharField(
			widget=forms.TextInput(attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
			label='نام و نام خانوادگی',
		)

	email = forms.EmailField(
			widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': 'form-control'}),
			label='ایمیل',

		)
	subject = forms.CharField(
			widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان خود را وارد نمایید', 'class': 'form-control'}),
			label='عنوان',

		)
	text = forms.CharField(
			widget=forms.Textarea(attrs={'placeholder': 'متن پیام', 'class': 'form-control'}),
			label='متن پیام',

		)