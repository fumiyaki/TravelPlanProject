import { Component } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router'
import { Http, URLSearchParams, Headers }  from '@angular/http';

import { TourismSpot } from './tourismspot.model'

@Component({
  selector: 'my-app',
  templateUrl: `./templates/create.component.html`,
  styleUrls: ['./static/create.component.css'],
})
export class CreateComponent {
  tss: any = [];
  s_tss: TourismSpot[] = [];
  search_spot: string;
  route_plan_id: string;
  routeplan = {
    name: '',
    desc: '',
    user: '',
  }

  constructor(private route: ActivatedRoute, private http: Http) {
    let user_id: string = localStorage.getItem('token');
    if( !user_id ){
      location.href = "./login";
    }
  }

  ngOnInit() {
    this.route.queryParams.subscribe( params => this.route_plan_id = `${params['route_plan_id']}` );

    if( this.route_plan_id !== "" ){
      let route_plan_spots: any = [];
      this.http.get('http://127.0.0.1:8000/api/routeplanspot/', {
        params: { route_plan: this.route_plan_id },
      }).subscribe(
        response => {
          // console.log("route_plan_spots",response.text())
          route_plan_spots = response.json();
        },
        error => {
          console.log(`通信失敗：${error.statusText}`)
        }
      );
      setTimeout(()=>{
        for(let route_plan_spot of route_plan_spots){
          this.http.get('http://127.0.0.1:8000/api/tourismspot/', {
            params: { id: route_plan_spot['spot'] },
          }).subscribe(
            response => {
              let tmp = response.json()
              this.tss.push(tmp[0]);
            },
            error => {
              console.log(`通信失敗：${error.statusText}`)
            }
          );
        }
      },100)

      setTimeout(()=>{
        let routeplanspot_order_num: any = []
        for(let i = 0; i < route_plan_spots.length; i++){
          for(let spot of this.tss){
            if(route_plan_spots[i]['spot'] == spot['id']){
              routeplanspot_order_num.push(spot)
              break
            }
          }
        }
        this.tss = routeplanspot_order_num
      },300)
      // setTimeout(()=>{
      //   console.log(this.tss)
      // },1500)
    }

    // 以下ドラッグ＆ドロップを実現するためのコード
    let dragSrcEl: any = null;
    function handleDragStart(e: any) {
      dragSrcEl = this;
      e.dataTransfer.effectAllowed = 'move';
      e.dataTransfer.setData('text/html', this.outerHTML);
      this.style.opacity = '0.4';
    }
    function handleDragOver(e: any) {
      if (e.preventDefault) {
        e.preventDefault();
      }
      e.dataTransfer.dropEffect = 'move';
      return false;
    }
    //dropされたところがdragされたところより高い場合true
    function checkBetterHeight(x:any,y:any){
      let int_x: number = parseInt(x.id)
      let int_y: number = parseInt(y.id)
      if(int_x>int_y){
        return true;
      }
       return false;
    }
    function liHandleDrop(e: any) {
      this.classList.remove('over');
      if (e.stopPropagation) {
        e.stopPropagation();
      }
      if (dragSrcEl != this) {
        if(dragSrcEl.parentNode == this.parentNode){
          if(checkBetterHeight(this,dragSrcEl)){
            this.outerHTML = this.outerHTML + e.dataTransfer.getData('text/html') ;
          }else{
            this.outerHTML =  e.dataTransfer.getData('text/html') + this.outerHTML;
          }
        }else{
          this.outerHTML = this.outerHTML + e.dataTransfer.getData('text/html');

        }
        dragSrcEl.outerHTML = "";

        ResetEvent();
      }
      return false;
    }
    function ulHandleDrop(e: any) {
      this.classList.remove('over');
      if (e.stopPropagation) {
        e.stopPropagation();
      }
      if (dragSrcEl != this) {
        dragSrcEl.outerHTML = "";
        this.innerHTML = this.innerHTML + e.dataTransfer.getData('text/html');
        ResetEvent();
      }
      return false;
    }
    function handleDragEnter(e: any) {
      this.classList.add('over');
    }
    function handleDragEnd(e: any) {
      this.style.opacity = '1.0';
    }
    function handleDragLeave(e: any) {
      this.classList.remove('over');
    }
    function ResetEvent() {
      let cols: any = document.querySelectorAll('.column');
      cols.forEach(function(col: any) {
        col.id="";
        col.removeEventListener('dragstart', handleDragStart, false);
        col.removeEventListener('dragenter', handleDragEnter, false);
        col.removeEventListener('dragover', handleDragOver, false);
        col.removeEventListener('dragleave', handleDragLeave, false);
        col.removeEventListener('drop', liHandleDrop, false);
        col.removeEventListener('dragend', handleDragEnd, false);
      });
      let i=1;
      cols.forEach(function(col: any) {
        col.id=i;
        i++
        col.addEventListener('dragstart', handleDragStart, false);
        col.addEventListener('dragenter', handleDragEnter, false);
        col.addEventListener('dragover', handleDragOver, false);
        col.addEventListener('dragleave', handleDragLeave, false);
        col.addEventListener('drop', liHandleDrop, false);
        col.addEventListener('dragend', handleDragEnd, false);
      });
      cols = document.querySelectorAll('.columns');
      cols.forEach(function(col: any) {
        col.removeEventListener('dragover', handleDragOver, false);
        col.removeEventListener('drop', ulHandleDrop, false);
      });
      cols.forEach(function(col: any) {
        col.addEventListener('dragover', handleDragOver, false);
        col.addEventListener('drop', ulHandleDrop, false);
      });
    }

    setInterval(ResetEvent, 500)

  }

  search() {
    this.http.get('http://127.0.0.1:8000/api/tourismspot/', {
      params: { name: this.search_spot },
    }).subscribe(
      response => {
        this.s_tss = response.json() as TourismSpot[];
      },
      error => {
        console.log(`通信失敗：${error.statusText}`);
      }
    );
  }

  post(e:any) {
    this.routeplan.user = localStorage.getItem('token');
    this.http.post('http://127.0.0.1:8000/api/routeplan/', this.routeplan)
    .subscribe(
    response => {
      let result = response.json()
      this.route_plan_id = result["id"]
      let result2 = response.text()
      // console.log(result2)
    },
    error => {
      console.log(`通信失敗：${error}`);
      }
    );

    let route_plan_spot: any = [];

    setTimeout(()=>{
      // htmlのclassを辿りspotのidを取得する
      let html_string: any = document.querySelector('.create_plan').innerHTML;
      let p = /<h4.*class="title_text" id="\d+.*">/gi;
      let p2 = /id="(\d)"/i;
      let results = html_string.match(p);
      for(let i = 0; i < results.length; i++){
        let result = results[i].match(p2);
        route_plan_spot.push(
          {
           route_plan: this.route_plan_id,
           spot: parseInt(result[1], 10),
           order_num: i
          }
        )
      }
      // console.log(route_plan_spot);
    }, 700)

    setTimeout(()=>{
      this.http.post('http://127.0.0.1:8000/api/routeplanspot/', route_plan_spot)
      .subscribe(
      response => {
        let result = response.text()
        // console.log(result)
        location.href = `./route-plan/${this.route_plan_id}`;
      },
      error => {
        console.log(`通信失敗：${error}`);
        }
      );
    },1500)
  }
}
