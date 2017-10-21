import { Component } from '@angular/core';
import { Http }  from '@angular/http';


@Component({
  selector: 'my-app',
    templateUrl: `./templates/route-plans.component.html`,
})
export class RoutePlansComponent {
routeplans:any = []
  constructor(private http: Http) { }

  ngOnInit(){
    this.http.get('http://127.0.0.1:8000/api/routeplan/')
    .subscribe(
      response => {
        this.routeplans = response.json();
      },
      error => {
        console.log(`通信失敗：${error.statusText}`);
      }
    );
  }
}
