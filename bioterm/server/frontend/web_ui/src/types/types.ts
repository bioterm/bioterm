export interface Controller {
  id: number;
  registration_date: string;
  uuid: string;
  display_name: string | null;
  description: string | null;
}

export interface Device {
  id: number;
  uuid: string;
  controller_id: number;
  display_name: string | null;
  registration_date: string;
  description: string | null;
  parameters: Record<string, unknown>;
  measurement_model: Record<string, unknown>;
  rpc: Record<string, RPCParam[]>;
  grafana_link: string | null;
}

export interface Dashboard {
  id: number;
  link: string;
  uid: string;
  controller_id: number;
}

export interface Panel {
  id: number;
  link: string;
  device_id: number;
  hidden: boolean;
}

export type ReturnType = "<class 'int'>" | "<class 'str'>";

export type PythonToTypeScriptTypes = {
  "<class 'int'>": number;
  "<class 'float'>": number;
  "<class 'str'>": string;
};

export interface RPCCommon {
  id?: string;
  name?: string;
  return_type: ReturnType;
}

export interface RPCWithRange extends RPCCommon {
  maxValue: number;
  minValue: number;
  increment: number;
}

export interface RPCWithRegex extends RPCCommon {
  regex: string;
}

// export type RPCParam = RPCWithRange | RPCWithRegex;

export type RPCParam = {
  id: string;
  name: string;
  maxValue?: number;
  minValue?: number;
  increment?: number;
  regex?: string;
  return_type: keyof PythonToTypeScriptTypes; // Change the type here
};

export type RPCs = Record<string, RPCParam[]>;

// export interface RPCs {
//   [key: string]: RPCParam[];
// }
