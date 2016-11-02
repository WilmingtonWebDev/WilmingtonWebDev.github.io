Title: Home
URL:
Date: 2016-10-28
Modified: 2016-11-02
Status: published
save_as: index.html

Welcome to _Wilmington Web Devs!_

### We're just getting started

There's not much here yet, but if you work web development and would be interested in comming to a meetup to share ideas, talk about best practices or or just talk to others who work in the sector this might be a meetup for you.

### The first meetup

Matts busy updating his meetup account and creating a group so that everyone can send in their lovely RSVPs.

We'll be trying out a lunchtime MeetUp at [The Mill Space](http://themillspace.com/) sometime towards the end of November.

It will provisionally be a meet & greet with a short Javascript talk on Promises in which we mostly likely try to cover:

  * What are they?
  * How they help you avoid callback hell and write better code.
  * Native ES2015 Promises vs Bluebird

### Get in touch

Whilst we're getting our ducks in a row you can contact us [@ThomasMarks](https://twitter.com/ThomasMarks)

---

**// Callback Hell**
```
getData(function(x){
    getMoreData(x, function(y){
      getMoreData(x, function(y){
        getMoreData(x, function(y){
            getMoreData(y, function(z){
                ...
            });
        });
      });
    });
});
```

**// Promisified **
```
getDataPromise
  .then(getData)
  .then(getData)
  .then(getData)
  .then(getData)
...
  .catch(handleError)
```
