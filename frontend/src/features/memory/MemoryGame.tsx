import React, { useState, useEffect } from 'react';
import { ArrowLeft, RotateCcw } from 'lucide-react';
import confetti from 'canvas-confetti';
import { Button } from '../../components/ui/Button';

interface MemoryGameProps {
  onBack: () => void;
  onComplete: (score: number) => void;
}

interface CardItem {
  id: number;
  symbol: string;
  name: string;
  isFlipped: boolean;
  isMatched: boolean;
}

const SYMBOLS = [
  { symbol: '🦁', name: 'Sher' },
  { symbol: '🐼', name: 'Panda' },
  { symbol: '🐰', name: 'Quyon' },
  { symbol: '🐬', name: 'Delfin' },
];

export const MemoryGame: React.FC<MemoryGameProps> = ({ onBack, onComplete }) => {
  const [cards, setCards] = useState<CardItem[]>([]);
  const [selectedCards, setSelectedCards] = useState<number[]>([]);
  const [moves, setMoves] = useState(0);
  const [isLocked, setIsLocked] = useState(false);

  const initGame = () => {
    const deck: CardItem[] = [];
    let id = 0;
    SYMBOLS.forEach((item) => {
      deck.push({ id: id++, symbol: item.symbol, name: item.name, isFlipped: false, isMatched: false });
      deck.push({ id: id++, symbol: item.symbol, name: item.name, isFlipped: false, isMatched: false });
    });
    // Shuffle
    deck.sort(() => Math.random() - 0.5);
    setCards(deck);
    setSelectedCards([]);
    setMoves(0);
    setIsLocked(false);
  };

  useEffect(() => {
    initGame();
  }, []);

  const handleCardClick = (index: number) => {
    if (isLocked) return;
    if (cards[index].isFlipped || cards[index].isMatched) return;

    const newCards = [...cards];
    newCards[index].isFlipped = true;
    setCards(newCards);

    const newSelected = [...selectedCards, index];
    setSelectedCards(newSelected);

    if (newSelected.length === 2) {
      setIsLocked(true);
      setMoves((m) => m + 1);

      const [firstIdx, secondIdx] = newSelected;
      if (newCards[firstIdx].symbol === newCards[secondIdx].symbol) {
        // Match!
        newCards[firstIdx].isMatched = true;
        newCards[secondIdx].isMatched = true;
        setCards(newCards);
        setSelectedCards([]);
        setIsLocked(false);

        // Check if all matched
        if (newCards.every((c) => c.isMatched)) {
          confetti({ particleCount: 80, spread: 80, origin: { y: 0.6 } });
          setTimeout(() => onComplete(10), 1000);
        }
      } else {
        // No match -> flip back after 800ms
        setTimeout(() => {
          newCards[firstIdx].isFlipped = false;
          newCards[secondIdx].isFlipped = false;
          setCards([...newCards]);
          setSelectedCards([]);
          setIsLocked(false);
        }, 800);
      }
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-4 flex flex-col gap-5">
      {/* Top Header */}
      <div className="flex items-center justify-between bg-white rounded-3xl p-4 shadow-md border-2 border-emerald-100">
        <Button variant="outline" size="md" onClick={onBack} className="gap-2">
          <ArrowLeft size={22} />
          <span>Orqaga</span>
        </Button>

        <h2 className="text-xl sm:text-2xl font-black text-gray-800">
          🧠 Xotira o‘yini
        </h2>

        <div className="flex items-center gap-3">
          <span className="text-sm font-bold text-gray-600 bg-gray-100 px-3 py-1.5 rounded-xl">
            Urinish: {moves}
          </span>
          <button
            onClick={initGame}
            className="p-2.5 rounded-2xl bg-amber-50 text-amber-700 hover:bg-amber-100 min-h-[44px] min-w-[44px] flex items-center justify-center transition-all"
            aria-label="Qayta boshlash"
          >
            <RotateCcw size={22} />
          </button>
        </div>
      </div>

      {/* Grid of Cards */}
      <div className="grid grid-cols-4 gap-3 sm:gap-4 bg-white rounded-3xl p-6 shadow-xl border-4 border-purple-200">
        {cards.map((card, idx) => (
          <button
            key={card.id}
            onClick={() => handleCardClick(idx)}
            className={`aspect-square rounded-2xl sm:rounded-3xl text-4xl sm:text-6xl font-black flex items-center justify-center transition-all duration-300 transform select-none cursor-pointer ${
              card.isFlipped || card.isMatched
                ? 'bg-gradient-to-tr from-amber-100 to-amber-200 shadow-md rotate-y-180 scale-100'
                : 'bg-gradient-to-tr from-purple-500 to-indigo-600 shadow-lg hover:scale-105 active:scale-95'
            }`}
          >
            {card.isFlipped || card.isMatched ? (
              <span>{card.symbol}</span>
            ) : (
              <span className="text-white text-3xl opacity-80">❓</span>
            )}
          </button>
        ))}
      </div>
    </div>
  );
};
