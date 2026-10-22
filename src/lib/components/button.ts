import { cva, type VariantProps } from 'class-variance-authority';

export const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-medium focus-ring disabled-state transition-colors',
  {
    variants: {
      variant: {
        default: 'bg-accent-500 text-white hover:bg-accent-600',
        secondary: 'bg-accent-secondary-500 text-white hover:bg-accent-secondary-600',
        outline: 'border border-border bg-background hover:bg-muted',
        ghost: 'hover:bg-muted',
        link: 'text-accent-500 underline-offset-4 hover:underline',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);

export interface ButtonProps
  extends VariantProps<typeof buttonVariants> {
  class?: string;
}
