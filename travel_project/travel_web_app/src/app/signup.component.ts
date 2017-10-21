import { Component } from '@angular/core';
import { Http, URLSearchParams, Headers }  from '@angular/http';

@Component({
  selector: 'my-app',
    templateUrl: `./templates/signup.component.html`,
})
export class SignupComponent {
  user = {
    user_id: '',
    password: '',
    name: '',
    gender: '',
    address: '',
  };

  constructor(private http: Http) { }

  signup() {
    // ハマりどころ？paramsの部分はURLSearchParamsは使えないJSON形式のみ？受け付けるっぽい
    this.http.post('http://127.0.0.1:8000/api/users/', this.user)
    .subscribe(
    response => {
      let result = response.json()
      localStorage.setItem('token', result['user_id']);
      location.href = "./";
    },
    error => {
      console.log(`通信失敗：${error}`);
      }
    );
  }
}
