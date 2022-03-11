import { defineRule,configure } from 'vee-validate';
import AllRules from '@vee-validate/rules';

configure({
  validateOnInput: true
});

Object.keys(AllRules).forEach(rule => {
  defineRule(rule, AllRules[rule]);
});

export default {};