from django.db import models
from django.db.models.signals import post_save
from UserAuthAPI.models import User
import uuid
# Create your models here.


class AccountBalance(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class TransactionType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
    is_disabled = models.BooleanField(default=False)
    is_effective = models.BooleanField(default=True)
    is_expense = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=500,null=True, blank=True)

class TransactionReview(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    is_auto_created = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    operator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    note = models.CharField(max_length=500,null=True, blank=True)


class Invoice(models.Model):
    '''
    Store the invoice that needs to apply for reimbursement
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_disabled = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    related_transactions = models.OneToOneField(Transaction, on_delete=models.CASCADE,null=True,blank=True)
    uploader = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    abn_number = models.CharField(max_length=11)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=500,null=True, blank=True)
    pic_scan = models.ImageField(upload_to='finance/invoices/', height_field=None, width_field=None, 
        blank=True, null=True)

    def _bind_transactions(self, created=False):
        if created:
            new_transaction = Transaction.objects.create(
                amount = self.amount,
                is_expense = True,
                transaction_type = TransactionType.objects.get(name='Lodge Expense'),
                is_effective = False,
            )
            self.__class__.objects.filter(id=self.id).update(
                related_transactions = new_transaction
            )


    def save(self, *args, **kwargs):
        created = self._state.adding
        super(Invoice, self).save(*args, **kwargs)
        print("New Record Status: "+ str(created))
        self._bind_transactions(created)




class BankTransferRecipient(models.Model):
    '''
    Store the bank transfer paid that needs to be checked
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_disabled = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    related_transactions = models.OneToOneField(Transaction, on_delete=models.CASCADE,null=True,blank=True)
    bsb = models.CharField(max_length=6)
    acc_number = models.CharField(max_length=11)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pic_scan = models.ImageField(upload_to='finance/bankreceipient/', height_field=None, width_field=None, 
        blank=True, null=True)
    note = models.CharField(max_length=500,null=True, blank=True)    
