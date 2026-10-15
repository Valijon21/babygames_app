import React from 'react';

interface CardProps {
  className?: string;
  children: React.ReactNode;
  onClick?: () => void;
}

export const Card: React.FC<CardProps> = ({ className = '', children, onClick }) => {
  return (
    <div
      onClick={onClick}
      className={`bg-white rounded-3xl p-6 border-2 border-emerald-100 shadow-lg hover:shadow-xl transition-all ${
        onClick ? 'cursor-pointer hover:-translate-y-1 active:scale-98' : ''
      } ${className}`}
    >
      {children}
    </div>
  );
};
