import { Component } from '@angular/core';
import { Http, URLSearchParams, Headers }  from '@angular/http';

@Component({
  selector: 'my-app',
    templateUrl: `./templates/login.component.html`,
})
export class LoginComponent {
  login_user = {
    user_id: '',
    passwd: '',
  };
  result: any;
  err: String;

  constructor(private http: Http) { }

  login() {
    this.http.get('http://127.0.0.1:8000/api/users/', {
      params: { user_id: this.login_user.user_id, password: this.login_user.passwd},
      }).subscribe(
      response => {
        this.result = response.json();
        if( this.result.length === 1 ){
          localStorage.setItem('token', this.result[0]['user_id']);
          this.err = "";
          location.href = "./";
        }else{
          this.err = "ユーザーIDまたはパスワードが間違っています";
        }
      },
      error => {
        this.result = `通信失敗：${error.statusText}`;
      }
    );
  }
}
