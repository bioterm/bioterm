import { Notify } from 'quasar';

export function showSuccess(message: string): void {
  Notify.create({
    type: 'positive',
    message: message,
    position: 'bottom',
    textColor: 'white',
    actions: [
      {
        icon: 'close',
        color: 'white',
        round: true,
        size: '10px',
        class: 'q-ml-auto',
      },
    ],
  });
}

export function showError(message: string): void {
  Notify.create({
    type: 'negative',
    message: message,
    position: 'bottom',
    actions: [
      {
        icon: 'close',
        color: 'white',
        round: true,
        size: '10px',
        class: 'q-ml-auto',
      },
    ],
  });
}
