//- TypeScript 1.4 source code

//- quanah.d.ts ~~
//
//  This file defines Quanah as an "ambient external module" for TypeScript :-)
//
//                                                      ~~ (c) SRW, 13 Mar 2015
//                                                  ~~ last updated 16 Mar 2015

declare module "quanah" {

    interface AVar {
        on(name: string, listener: Listener): AVar;
        Q(f: AVar | Transform): AVar;
        send(name: string, arg?: any): AVar;
        val: any;
    }

    interface Listener {
        (message?: any): void;
    }

    interface Task {
        f: Transform;
        x: AVar;
    }

    interface Transform {
        call(that: AVar, signal: {
            exit: Listener;
            fail: Listener;
            stay: Listener;
        }): void;
    }

    export function avar(val?: any): AVar;

    export function canRunRemotely(task: Task): boolean;    // user-provided

    export function runRemotely(task: Task): void;          // user-provided

    export function snooze(tick: () => void): any;          // user-provided

    export function sync(... any): AVar;

}

//- vim:set syntax=typescript:
