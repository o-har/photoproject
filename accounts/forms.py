# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス
        Attributes:
          model:連携するUserモデル
          fields:フォームで使用するフィールド
        '''
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')