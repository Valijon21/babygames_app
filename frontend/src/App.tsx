import React, { useState, useEffect } from 'react';
import { Navbar } from './components/layout/Navbar';
import { GameCard } from './features/catalog/GameCard';
import { ColoringGame } from './features/coloring/ColoringGame';
import { AlphabetGame } from './features/alphabet/AlphabetGame';
import { NumbersGame } from './features/numbers/NumbersGame';
import { MemoryGame } from './features/memory/MemoryGame';
import { ResultsModal } from './features/progress/ResultsModal';
import { ParentGateModal } from './features/parent/ParentGateModal';
import { ParentDashboardModal } from './features/parent/ParentDashboardModal';
import { fetchGames, submitGameSession } from './lib/api';
import { Game, AgeBand, ChildProfile } from './types';
import { Sparkles, Palette, BookOpen, Calculator, Brain } from 'lucide-react';

export const App: React.FC = () => {
  const [selectedAge, setSelectedAge] = useState<AgeBand | 'all'>('all');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [games, setGames] = useState<Game[]>([]);
  const [activeGame, setActiveGame] = useState<Game | null>(null);
  const [sessionStartTime, setSessionStartTime] = useState<number>(0);
  const [soundEnabled, setSoundEnabled] = useState<boolean>(true);

  // Modals
  const [resultModalOpen, setResultModalOpen] = useState(false);
  const [latestScore, setLatestScore] = useState(10);
  const [parentGateOpen, setParentGateOpen] = useState(false);
  const [parentDashboardOpen, setParentDashboardOpen] = useState(false);

  // Child profiles state
  const [children, setChildren] = useState<ChildProfile[]>([
    {
      id: 'default-child-1',
      display_name: 'Azizbek',
      age_band: '5-7',
      avatar_key: 'avatar_bear',
      preferences: { sound_enabled: true },
    },
  ]);

  useEffect(() => {
    fetchGames().then((data) => setGames(data));
  }, []);

  const handleLaunchGame = (game: Game) => {
    setActiveGame(game);
    setSessionStartTime(Date.now());
  };

  const handleCompleteGame = async (score: number) => {
    const duration = Math.round((Date.now() - sessionStartTime) / 1000);
    setLatestScore(score);
    setResultModalOpen(true);

    if (activeGame) {
      await submitGameSession({
        game_slug: activeGame.slug,
        duration_seconds: duration,
        score,
        completed: true,
      });
    }
  };

  const handleAddChild = (name: string, ageBand: AgeBand) => {
    const newChild: ChildProfile = {
      id: `child-${Date.now()}`,
      display_name: name,
      age_band: ageBand,
      avatar_key: 'avatar_star',
      preferences: { sound_enabled: true },
    };
    setChildren([...children, newChild]);
  };

  const handleDeleteChild = (id: string) => {
    setChildren(children.filter((c) => c.id !== id));
  };

  // Filter games by age and category
  const filteredGames = games.filter((game) => {
    if (selectedCategory !== 'all' && game.category_slug !== selectedCategory) {
      return false;
    }
    if (selectedAge !== 'all') {
      const [minStr, maxStr] = selectedAge.split('-');
      const min = parseInt(minStr, 10);
      const max = parseInt(maxStr, 10);
      if (game.max_age < min || game.min_age > max) {
        return false;
      }
    }
    return true;
  });

  const categories = [
    { slug: 'all', label: 'Barchasi', icon: Sparkles },
    { slug: 'coloring', label: 'Rasm bo‘yash', icon: Palette },
    { slug: 'alphabet', label: 'Alifbo', icon: BookOpen },
    { slug: 'numbers', label: 'Raqamlar', icon: Calculator },
    { slug: 'memory', label: 'Xotira', icon: Brain },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-b from-sky-50 via-emerald-50 to-amber-50">
      {/* Navigation Bar */}
      <Navbar
        selectedAge={selectedAge}
        onSelectAge={setSelectedAge}
        soundEnabled={soundEnabled}
        onToggleSound={() => setSoundEnabled(!soundEnabled)}
        onOpenParentGate={() => setParentGateOpen(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-6xl w-full mx-auto px-4 py-6">
        {activeGame ? (
          <div>
            {activeGame.category_slug === 'coloring' && (
              <ColoringGame
                onBack={() => setActiveGame(null)}
                onComplete={handleCompleteGame}
              />
            )}
            {activeGame.category_slug === 'alphabet' && (
              <AlphabetGame
                onBack={() => setActiveGame(null)}
                onComplete={handleCompleteGame}
              />
            )}
            {activeGame.category_slug === 'numbers' && (
              <NumbersGame
                onBack={() => setActiveGame(null)}
                onComplete={handleCompleteGame}
              />
            )}
            {activeGame.category_slug === 'memory' && (
              <MemoryGame
                onBack={() => setActiveGame(null)}
                onComplete={handleCompleteGame}
              />
            )}
          </div>
        ) : (
          <div className="flex flex-col gap-6">
            {/* Cheerful Hero Banner */}
            <div className="bg-gradient-to-r from-blue-500 via-indigo-500 to-pink-500 rounded-3xl p-6 sm:p-8 text-white shadow-xl flex flex-col sm:flex-row items-center justify-between gap-6 relative overflow-hidden">
              <div className="max-w-xl text-center sm:text-left z-10">
                <span className="px-3.5 py-1 rounded-full bg-white/20 text-xs font-black uppercase tracking-wider backdrop-blur-xs">
                  O‘rganamiz va o‘ynaymiz!
                </span>
                <h2 className="text-3xl sm:text-4xl font-black mt-2 leading-tight">
                  Salom, jajji do‘stim! 🌟
                </h2>
                <p className="mt-2 text-blue-100 font-bold text-base sm:text-lg">
                  Bugun qaysi qiziqarli o‘yinni o‘ynashni xohlaysan?
                </p>
              </div>

              <div className="text-7xl sm:text-8xl drop-shadow-lg select-none z-10 animate-bounce">
                🚀
              </div>
            </div>

            {/* Category Filter Tabs */}
            <div className="flex items-center gap-2 overflow-x-auto pb-2">
              {categories.map((cat) => {
                const Icon = cat.icon;
                const isActive = selectedCategory === cat.slug;
                return (
                  <button
                    key={cat.slug}
                    onClick={() => setSelectedCategory(cat.slug)}
                    className={`px-4 py-2.5 rounded-2xl font-black text-sm flex items-center gap-2 whitespace-nowrap transition-all min-h-[48px] cursor-pointer ${
                      isActive
                        ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/25 scale-105'
                        : 'bg-white text-gray-700 hover:bg-gray-50 border border-gray-200'
                    }`}
                  >
                    <Icon size={18} />
                    <span>{cat.label}</span>
                  </button>
                );
              })}
            </div>

            {/* Games Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
              {filteredGames.map((game) => (
                <GameCard
                  key={game.id}
                  game={game}
                  onPlay={handleLaunchGame}
                />
              ))}
            </div>

            {filteredGames.length === 0 && (
              <div className="bg-white rounded-3xl p-12 text-center border-2 border-dashed border-gray-300">
                <p className="text-lg font-bold text-gray-600">
                  Ushbu toifa uchun hozircha o‘yinlar topilmadi.
                </p>
                <button
                  onClick={() => {
                    setSelectedAge('all');
                    setSelectedCategory('all');
                  }}
                  className="mt-4 px-5 py-2.5 bg-blue-500 text-white font-bold rounded-2xl hover:bg-blue-600 transition-all cursor-pointer"
                >
                  Barcha o‘yinlarni ko‘rish
                </button>
              </div>
            )}
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="mt-auto border-t border-emerald-100 bg-white/80 py-4 px-4 text-center text-xs font-bold text-gray-500">
        <p>© 2026 Bolajon — Bolalar uchun xavfsiz va ta’limiy o‘yinlar platformasi.</p>
      </footer>

      {/* Completion Modal */}
      <ResultsModal
        isOpen={resultModalOpen}
        score={latestScore}
        onReplay={() => {
          setResultModalOpen(false);
          setSessionStartTime(Date.now());
        }}
        onContinue={() => {
          setResultModalOpen(false);
          setActiveGame(null);
        }}
      />

      {/* Parent Gate Modal */}
      <ParentGateModal
        isOpen={parentGateOpen}
        onClose={() => setParentGateOpen(false)}
        onSuccess={() => {
          setParentGateOpen(false);
          setParentDashboardOpen(true);
        }}
      />

      {/* Parent Dashboard Modal */}
      <ParentDashboardModal
        isOpen={parentDashboardOpen}
        onClose={() => setParentDashboardOpen(false)}
        childrenProfiles={children}
        onAddChild={handleAddChild}
        onDeleteChild={handleDeleteChild}
      />
    </div>
  );
};

export default App;
