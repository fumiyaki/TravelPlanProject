import { Component } from '@angular/core';
import { Http }  from '@angular/http';

@Component({
  selector: 'my-app',
  templateUrl: `./templates/mypage.component.html`,
})
export class MypageComponent {

  routeplans:any = []
  user = {
    user_id: '',
    password: '',
    name: '',
    gender: '',
    address: '',
  };
  result: any;

  constructor(private http: Http) { }

  ngOnInit() {

    this.user.user_id = localStorage.getItem('token');

    if( localStorage.getItem('token') === null ){
      this.user.user_id = "";
      location.href = "./login";
    }

    this.http.get('http://127.0.0.1:8000/api/users/', {
      params: { user_id: this.user.user_id },
    }).subscribe(
      response => {
        this.result = response.json();
        if(this.result.length === 1){
          this.user.user_id = this.result[0]["user_id"];
          this.user.name = this.result[0]["name"];
          this.user.gender = this.result[0]["gender"];
          this.user.address = this.result[0]["address"];
        }
      },
      error => {
        console.log(`通信失敗：${error.statusText}`);
      }
    );

    this.http.get('http://127.0.0.1:8000/api/routeplan/', {
      params: { user: this.user.user_id },
    }).subscribe(
      response => {
        this.routeplans = response.json();
      },
      error => {
        console.log(`通信失敗：${error.statusText}`);
      }
    );
  }
}
