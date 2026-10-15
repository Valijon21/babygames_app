import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'accent' | 'outline';
  size?: 'md' | 'lg';
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  className = '',
  children,
  ...props
}) => {
  const baseClasses =
    'inline-flex items-center justify-center font-bold rounded-2xl cursor-pointer select-none transition-all active:scale-95 shadow-md focus:outline-none focus:ring-4 focus:ring-blue-300 disabled:opacity-50 disabled:cursor-not-allowed';

  const sizeClasses = {
    md: 'px-5 py-3 text-base min-h-[48px] min-w-[48px]',
    lg: 'px-8 py-4 text-xl min-h-[56px] min-w-[56px]',
  };

  const variantClasses = {
    primary: 'bg-blue-500 hover:bg-blue-600 text-white shadow-blue-500/25',
    secondary: 'bg-pink-500 hover:bg-pink-600 text-white shadow-pink-500/25',
    accent: 'bg-amber-400 hover:bg-amber-500 text-amber-950 shadow-amber-400/25',
    outline: 'border-3 border-blue-400 text-blue-600 hover:bg-blue-50 bg-white',
  };

  return (
    <button
      className={`${baseClasses} ${sizeClasses[size]} ${variantClasses[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};
