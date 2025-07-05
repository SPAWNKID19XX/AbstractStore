// src/components/ui/card.tsx
import React from "react";

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {}

export const Card: React.FC<CardProps> = ({ children, className = "", ...props }) => (
  <div
    className={`bg-white shadow-md rounded-lg p-6 border border-gray-200 ${className}`}
    {...props}
  >
    {children}
  </div>
);

export const CardHeader: React.FC<CardProps> = ({ children, className = "", ...props }) => (
  <div className={`mb-4 font-semibold text-lg ${className}`} {...props}>
    {children}
  </div>
);

export const CardTitle: React.FC<CardProps> = ({ children, className = "", ...props }) => (
  <h2 className={`text-xl font-bold mb-2 ${className}`} {...props}>
    {children}
  </h2>
);

export const CardContent: React.FC<CardProps> = ({ children, className = "", ...props }) => (
  <div className={`text-gray-700 ${className}`} {...props}>
    {children}
  </div>
);

export default Card;
