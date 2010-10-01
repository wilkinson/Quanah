//- JavaScript source code -- Web Worker script

//- bee.js ~~
//  This is where the magic happens. The computational nodes poll a URL where
//  tasks needing to be accomplished are posted by a CouchDB filter rule. The
//  node then executes the first task listed and uploads its results. Each task
//  itself runs within a fresh Web Worker context (a special JS sandbox) and
//  then exits immediately. There is a "setTimeout loop" that creates another
//  worker when this one closes.
//                                                          ~~ SRW, 27 Sep 2010

importScripts("Q.js");

Q.merge(Q, this);                       //- gives Jonas the syntax he wanted :)

var changes = Q.couch.read("_changes?filter=quanah/code"),
    latest = {},
    results = changes.results || [];

if (results.length > 0) {

    latest = Q.couch.read(results[0].id);
    latest.volunteer = Q.whoami();
    latest.results = Q.run(latest.code);
    Q.couch.write(latest);              //- security hole for server?

}

var t = 1000;                           //- milliseconds till Worker closes
postMessage(t);
setTimeout(close, t);

//- vim:set syntax=javascript: