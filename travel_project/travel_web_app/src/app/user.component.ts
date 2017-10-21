import { Component } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router'
import { Http }  from '@angular/http';


@Component({
  selector: 'my-app',
    templateUrl: `./templates/user.component.html`,
})
export class UserComponent {
  user = {
    user_id: '',
    password: '',
    name: '',
    gender: '',
    address: '',
  };
  routeplans:any = []

  constructor(private route: ActivatedRoute, private http: Http) { }

  ngOnInit() {
  this.route.params.subscribe(
    params => this.user.user_id = params['id']);

    this.http.get('http://127.0.0.1:8000/api/users/', {
      params: { user_id: this.user.user_id },
    }).subscribe(
      response => {
        this.user = response.json()[0];
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
