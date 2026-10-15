import React from 'react';
import { Play, Clock } from 'lucide-react';
import { Game } from '../../types';
import { Card } from '../../components/ui/Card';

interface GameCardProps {
  game: Game;
  onPlay: (game: Game) => void;
}

export const GameCard: React.FC<GameCardProps> = ({ game, onPlay }) => {
  const categoryThemes: Record<string, { bg: string; border: string; badge: string; icon: string }> = {
    coloring: { bg: 'from-pink-50 to-rose-100', border: 'border-pink-200', badge: 'bg-pink-100 text-pink-700', icon: '🎨' },
    alphabet: { bg: 'from-blue-50 to-sky-100', border: 'border-blue-200', badge: 'bg-blue-100 text-blue-700', icon: '🔤' },
    numbers: { bg: 'from-emerald-50 to-green-100', border: 'border-emerald-200', badge: 'bg-emerald-100 text-emerald-700', icon: '🔢' },
    memory: { bg: 'from-purple-50 to-indigo-100', border: 'border-purple-200', badge: 'bg-purple-100 text-purple-700', icon: '🧠' },
  };

  const theme = categoryThemes[game.category_slug] || {
    bg: 'from-amber-50 to-orange-100',
    border: 'border-amber-200',
    badge: 'bg-amber-100 text-amber-700',
    icon: '✨',
  };

  return (
    <Card
      onClick={() => onPlay(game)}
      className={`border-4 ${theme.border} bg-gradient-to-br ${theme.bg} flex flex-col justify-between overflow-hidden relative group`}
    >
      <div>
        {/* Top Badges */}
        <div className="flex items-center justify-between mb-3">
          <span className={`text-xs font-black px-3 py-1 rounded-full uppercase tracking-wider ${theme.badge}`}>
            {game.category_title}
          </span>
          <span className="text-xs font-bold bg-white/80 text-gray-700 px-2.5 py-1 rounded-full shadow-2xs">
            {game.min_age}–{game.max_age} yosh
          </span>
        </div>

        {/* Big Illustration Emoji */}
        <div className="text-6xl text-center my-3 group-hover:scale-115 transition-transform duration-300 drop-shadow-md">
          {theme.icon}
        </div>

        {/* Title */}
        <h3 className="text-xl font-black text-gray-900 text-center mb-1 group-hover:text-blue-600 transition-colors">
          {game.title}
        </h3>

        {/* Duration */}
        <div className="flex items-center justify-center gap-1.5 text-xs font-bold text-gray-500 mb-4">
          <Clock size={14} />
          <span>Taxminan {game.estimated_minutes} daqiqa</span>
        </div>
      </div>

      {/* Big Play Button */}
      <button
        onClick={(e) => {
          e.stopPropagation();
          onPlay(game);
        }}
        className="w-full py-3.5 px-4 rounded-2xl bg-blue-500 hover:bg-blue-600 active:scale-95 text-white font-black text-base flex items-center justify-center gap-2 shadow-md shadow-blue-500/20 transition-all cursor-pointer"
      >
        <Play size={20} className="fill-current" />
        <span>O‘ynash</span>
      </button>
    </Card>
  );
};
