import { Component } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Http }  from '@angular/http';


@Component({
  selector: 'my-app',
    templateUrl: `./templates/spot.component.html`,
})
export class SpotComponent {
  id = ''
  tourismspot = {
        id: 0,
        name: "",
        desc: "",
        prefecture: "",
        address: "",
        phone_num: "",
        parkinglot: 0,
        holiday: "",
        business_hours: "",
        charge: 0,
        coordinate_latitude: 0,
        coordinate_longitude: 0,
        grade: 0
  }

  constructor(private route: ActivatedRoute, private http: Http) { }

  ngOnInit() {
  this.route.params.subscribe(
    params => this.id = params['id'])

    this.http.get('http://127.0.0.1:8000/api/tourismspot/', {
      params: { id: this.id },
    }).subscribe(
      response => {
        this.tourismspot = response.json()[0]
      },
      error => {
        console.log(`通信失敗：${error.statusText}`)
      }
    );
  }
}
