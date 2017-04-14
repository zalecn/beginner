
export as namespace pomelo;
export interface initCallBack {
	(): void;
}
export interface anyCallBack {
	(data: any) : void;
}

export function init(options: Object, cb: initCallBack): void;
export function on(route: string, cb: anyCallBack): void;
export function request(route: string, param: Object, cb:anyCallBack) : void;
export function request(route: string, cb:anyCallBack) : void;
export function disconnect() : void;
