// export type Condition = LogicCondition | ValueCondition | TimeCondition;
export type Condition = LogicCondition | ValueCondition;

export interface BaseCondition {
  dwell?: number;
}

export interface LogicCondition extends BaseCondition {
  operator: 'AND' | 'OR';
  conditions: Condition[];
}

export interface ValueCondition extends BaseCondition {
  device: string;
  meas: string;
  value: string | number;
  operator: 'eq' | 'le' | 'leq' | 'ge' | 'geq' | 'neq';
}

// export interface TimeCondition extends BaseCondition {
//   value: number;
//   operator: 'time';
// }

export interface Argument {
  name: string;
  value: string | number;
}

export interface Method {
  name: string;
  arguments: Argument[];
}

export interface Rule {
  device: string;
  trigger_condition: Condition;
  trigger_method: Method;
  release_condition: Condition;
  release_method: Method;
}

export interface RuleModel {
  id: number | null;
  uuid: string | null;
  controller_id: number | null;
  sync: boolean;
  display_name: string;
  description: string;
  rule: Rule;
}

export interface RuleCreate {
  sync: boolean;
  display_name: string;
  description: string;
  rule: Rule;
}

export interface RuleUpdate {
  sync: boolean;
  display_name: string;
  description: string;
  rule: Rule;
}
