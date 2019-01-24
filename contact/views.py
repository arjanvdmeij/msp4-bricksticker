from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template.loader import render_to_string
from .forms import ContactForm

def contact(request):
    form = ContactForm
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            message = render_to_string(
                'contact_mail.html',{
                    'contact_name':form.cleaned_data['contact_name'],
                    'contact_email':form.cleaned_data['contact_email'],
                    'form_content': form.cleaned_data['content'],
                })
            mail_subject = 'Contactform Submission'
            email_to = 'ci.avdm@gmail.com'
            email = EmailMessage(mail_subject, message, to=[email_to])
            # email.content_subtype = 'html'
            email.send()
            
            
            
            # contact_name = request.POST.get(
            #     'contact_name'
            # , '')
            # contact_email = request.POST.get(
            #     'contact_email'
            # , '')
            # form_content = request.POST.get('content', '')

            # # Email the profile with the
            # # contact information
            # template = get_template('contact_mail.html')
            # context = {
            #     'contact_name': contact_name,
            #     'contact_email': contact_email,
            #     'form_content': form_content,
            # }
            # content = template.render(context)

            # email = EmailMessage(
            #     "New Message from Contactform submission",
            #     content,
            #     "Brickstickershop" +'',
            #     ['ci.avdm@gmail.com'],
            #     headers = {'Reply-To': contact_email }
            # )
            # email.send()
            return redirect('contact')
    
    return render(request, 'contact.html', {
        'form':form,
    })

# try:
#                     order_items = OrderItem.objects.filter(order=saved_order)
#                     site = get_current_site(request)
#                     message = render_to_string(
#                         'confirmation.html',{
#                             'order':saved_order,
#                             'order_items':order_items,
#                             'total': total,
#                             'site':site.domain,
#                         })
#                     mail_subject = 'Thank you for your order'
#                     email_to = order_form.cleaned_data['email_address']
#                     email = EmailMessage(mail_subject, message, to=[email_to])
#                     email.content_subtype = 'html'
#                     email.send()
#                 except BadHeaderError:
#                     return HttpResponse('Invalid header found.')
                
#                 messages.error(request, "You have successfully paid. Your order will be processed promptly.")
#                 request.session['cart'] = {}