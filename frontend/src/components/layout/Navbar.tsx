import React from 'react';
import { Sparkles, Volume2, VolumeX, ShieldCheck } from 'lucide-react';
import { AgeBand } from '../../types';

interface NavbarProps {
  selectedAge: AgeBand | 'all';
  onSelectAge: (age: AgeBand | 'all') => void;
  soundEnabled: boolean;
  onToggleSound: () => void;
  onOpenParentGate: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  selectedAge,
  onSelectAge,
  soundEnabled,
  onToggleSound,
  onOpenParentGate,
}) => {
  const ageOptions: Array<{ id: AgeBand | 'all'; label: string }> = [
    { id: 'all', label: 'Barchasi' },
    { id: '2-4', label: '2–4 yosh' },
    { id: '5-7', label: '5–7 yosh' },
    { id: '8-10', label: '8–10 yosh' },
  ];

  return (
    <header className="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b-2 border-emerald-100 px-4 py-3 shadow-xs">
      <div className="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-3">
        {/* Brand */}
        <div className="flex items-center gap-2 cursor-pointer" onClick={() => onSelectAge('all')}>
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-amber-400 to-pink-500 flex items-center justify-center text-white shadow-md">
            <Sparkles size={28} />
          </div>
          <div>
            <h1 className="text-2xl font-black tracking-tight text-blue-600 leading-none">
              Bolajon
            </h1>
            <span className="text-xs font-bold text-pink-500 uppercase tracking-wider">
              Ta’limiy o‘yinlar
            </span>
          </div>
        </div>

        {/* Age Band Pills */}
        <div className="flex items-center gap-1.5 overflow-x-auto py-1">
          {ageOptions.map((opt) => (
            <button
              key={opt.id}
              onClick={() => onSelectAge(opt.id)}
              className={`px-3.5 py-1.5 rounded-full text-sm font-bold transition-all min-h-[44px] flex items-center ${
                selectedAge === opt.id
                  ? 'bg-blue-500 text-white shadow-md scale-105'
                  : 'bg-emerald-50 text-emerald-800 hover:bg-emerald-100'
              }`}
            >
              {opt.label}
            </button>
          ))}
        </div>

        {/* Controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={onToggleSound}
            className="p-2.5 rounded-2xl bg-amber-50 text-amber-700 hover:bg-amber-100 border border-amber-200 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all"
            aria-label={soundEnabled ? 'Ovozni o‘chirish' : 'Ovozni yoqish'}
          >
            {soundEnabled ? <Volume2 size={24} /> : <VolumeX size={24} />}
          </button>

          <button
            onClick={onOpenParentGate}
            className="px-3.5 py-2 rounded-2xl bg-purple-50 text-purple-700 hover:bg-purple-100 border border-purple-200 min-h-[44px] flex items-center gap-1.5 text-sm font-bold transition-all"
          >
            <ShieldCheck size={20} />
            <span className="hidden sm:inline">Ota-ona</span>
          </button>
        </div>
      </div>
    </header>
  );
};
