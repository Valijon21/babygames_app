import React, { useEffect } from 'react';
import { Trophy, Star, RotateCcw, ArrowRight } from 'lucide-react';
import confetti from 'canvas-confetti';
import { Button } from '../../components/ui/Button';

interface ResultsModalProps {
  isOpen: boolean;
  score: number;
  onReplay: () => void;
  onContinue: () => void;
}

export const ResultsModal: React.FC<ResultsModalProps> = ({
  isOpen,
  score,
  onReplay,
  onContinue,
}) => {
  useEffect(() => {
    if (isOpen) {
      confetti({
        particleCount: 120,
        spread: 90,
        origin: { y: 0.5 },
      });
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm animate-fade-in">
      <div className="bg-white rounded-3xl max-w-sm w-full p-8 shadow-2xl border-4 border-amber-300 text-center flex flex-col items-center gap-5 animate-scale-up">
        {/* Trophy Icon */}
        <div className="w-24 h-24 rounded-full bg-amber-100 border-4 border-amber-400 flex items-center justify-center text-amber-500 shadow-lg animate-bounce">
          <Trophy size={48} />
        </div>

        <div>
          <h2 className="text-3xl font-black text-gray-800">
            Ajoyib natija! 🎉
          </h2>
          <p className="text-base font-bold text-emerald-600 mt-1">
            Siz barcha topshiriqlarni bajardingiz!
          </p>
        </div>

        {/* Stars */}
        <div className="flex items-center gap-2">
          {[1, 2, 3].map((s) => (
            <Star
              key={s}
              size={36}
              className="fill-amber-400 text-amber-500 drop-shadow-md animate-pulse"
            />
          ))}
        </div>

        <div className="text-lg font-bold text-gray-700 bg-gray-50 px-6 py-2.5 rounded-2xl w-full">
          Ball: <span className="text-blue-600 font-black text-2xl">{score} / 10</span>
        </div>

        <div className="flex flex-col w-full gap-3 mt-2">
          <Button variant="primary" size="lg" onClick={onContinue} className="gap-2 w-full">
            <span>Boshqa o‘yinlar</span>
            <ArrowRight size={22} />
          </Button>

          <Button variant="outline" size="md" onClick={onReplay} className="gap-2 w-full">
            <RotateCcw size={20} />
            <span>Qaytadan o‘ynash</span>
          </Button>
        </div>
      </div>
    </div>
  );
};
