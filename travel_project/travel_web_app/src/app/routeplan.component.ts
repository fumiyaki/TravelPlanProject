import { Component } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router'
import { Http }  from '@angular/http';


@Component({
  selector: 'my-app',
    templateUrl: `./templates/route-plan.component.html`,
})
export class RoutePlanComponent {
  id = ''
  routeplan:any = []
  routeplanspots:any = []
  tourismspots:any = []

  constructor(private route: ActivatedRoute, private http: Http) { }

  ngOnInit() {
  this.route.params.subscribe(
    params => this.id = params['id']);

    this.http.get('http://127.0.0.1:8000/api/routeplan/', {
      params: { id: this.id },
    }).subscribe(
      response => {
        this.routeplan = response.json()[0];
      },
      error => {
        console.log(`通信失敗：${error.statusText}`);
      }
    );
    setTimeout(() => {
      this.http.get('http://127.0.0.1:8000/api/routeplanspot/', {
        params: { route_plan: this.routeplan.id },
      }).subscribe(
        response => {
          this.routeplanspots = response.json();
        },
        error => {
          console.log(`通信失敗：${error.statusText}`);
        }
      );
    },100)

    setTimeout(() => {
      for(let routeplanspot of this.routeplanspots){
        this.http.get('http://127.0.0.1:8000/api/tourismspot/', {
          params: { id: routeplanspot.spot },
        }).subscribe(
          response => {
            this.tourismspots.push(response.json()[0]);
          },
          error => {
            console.log(`通信失敗：${error.statusText}`);
          }
        );
      }
    },500)

    setTimeout(()=>{
      let routeplanspot_order_num: any = []
      for(let i = 0; i < this.routeplanspots.length; i++){
        for(let spot of this.tourismspots){
          if(this.routeplanspots[i]['spot'] == spot['id']){
            routeplanspot_order_num.push(spot)
            break
          }
        }
      }
      this.tourismspots = routeplanspot_order_num
      console.log(routeplanspot_order_num)
    },800)
  }
}
