import React, { useState } from 'react';
import { User, Plus, Trash2, HeartHandshake } from 'lucide-react';
import { Modal } from '../../components/ui/Modal';
import { Button } from '../../components/ui/Button';
import { ChildProfile, AgeBand } from '../../types';

interface ParentDashboardModalProps {
  isOpen: boolean;
  onClose: () => void;
  childrenProfiles: ChildProfile[];
  onAddChild: (name: string, ageBand: AgeBand) => void;
  onDeleteChild: (id: string) => void;
}

export const ParentDashboardModal: React.FC<ParentDashboardModalProps> = ({
  isOpen,
  onClose,
  childrenProfiles,
  onAddChild,
  onDeleteChild,
}) => {
  const [isAdding, setIsAdding] = useState(false);
  const [newChildName, setNewChildName] = useState('');
  const [newChildAge, setNewChildAge] = useState<AgeBand>('5-7');

  const handleCreate = (e: React.FormEvent) => {
    e.preventDefault();
    if (newChildName.trim()) {
      onAddChild(newChildName.trim(), newChildAge);
      setNewChildName('');
      setIsAdding(false);
    }
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Ota-ona Boshqaruv Paneli">
      <div className="flex flex-col gap-6">
        {/* Child Profiles Section */}
        <div>
          <div className="flex items-center justify-between mb-3">
            <h3 className="font-bold text-gray-800 text-lg flex items-center gap-2">
              <User size={20} className="text-purple-600" />
              <span>Bolalar Profillari</span>
            </h3>
            {!isAdding && (
              <button
                onClick={() => setIsAdding(true)}
                className="px-3 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-purple-700 text-sm font-bold flex items-center gap-1.5 transition-all"
              >
                <Plus size={16} />
                <span>Yangi profil</span>
              </button>
            )}
          </div>

          {isAdding && (
            <form onSubmit={handleCreate} className="bg-purple-50 p-4 rounded-2xl mb-4 border border-purple-200 flex flex-col gap-3">
              <div>
                <label className="block text-xs font-bold text-gray-700 mb-1">Bolaning ismi yoki taxallusi:</label>
                <input
                  type="text"
                  value={newChildName}
                  onChange={(e) => setNewChildName(e.target.value)}
                  placeholder="Masalan: Dilshodbek"
                  className="w-full p-2.5 rounded-xl border border-gray-300 bg-white font-medium"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-gray-700 mb-1">Yosh toifasi:</label>
                <select
                  value={newChildAge}
                  onChange={(e) => setNewChildAge(e.target.value as AgeBand)}
                  className="w-full p-2.5 rounded-xl border border-gray-300 bg-white font-medium"
                >
                  <option value="2-4">2–4 yosh (Kichkintoylar)</option>
                  <option value="5-7">5–7 yosh (Maktabgacha)</option>
                  <option value="8-10">8–10 yosh (Boshlang‘ich)</option>
                  <option value="11-14">11–14 yosh (Kattaroq)</option>
                </select>
              </div>

              <div className="flex justify-end gap-2 mt-1">
                <Button variant="outline" size="md" type="button" onClick={() => setIsAdding(false)}>
                  Bekor qilish
                </Button>
                <Button variant="primary" size="md" type="submit" className="bg-purple-600 hover:bg-purple-700">
                  Saqlash
                </Button>
              </div>
            </form>
          )}

          <div className="flex flex-col gap-2.5">
            {childrenProfiles.map((child) => (
              <div
                key={child.id}
                className="flex items-center justify-between p-3.5 rounded-2xl bg-gray-50 border border-gray-200"
              >
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-black">
                    {child.display_name.charAt(0)}
                  </div>
                  <div>
                    <div className="font-bold text-gray-900">{child.display_name}</div>
                    <div className="text-xs text-gray-500 font-semibold">{child.age_band} yosh toifasi</div>
                  </div>
                </div>

                <button
                  onClick={() => onDeleteChild(child.id)}
                  className="p-2 text-gray-400 hover:text-red-500 rounded-xl hover:bg-red-50 transition-colors"
                  aria-label="Profilni o‘chirish"
                >
                  <Trash2 size={18} />
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Child Safety & Privacy Banner */}
        <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 flex items-start gap-3">
          <HeartHandshake className="text-emerald-600 shrink-0 mt-0.5" size={22} />
          <div className="text-xs text-emerald-900 leading-relaxed">
            <span className="font-bold block mb-0.5">Bolalar xavfsizligi kafolati:</span>
            Ushbu platformada reklama mavjud emas, ochiq chat yo‘q va bolalarning shaxsiy ma’lumotlari (telefon, manzil, to‘liq tug‘ilgan sana) yig‘ilmaydi.
          </div>
        </div>
      </div>
    </Modal>
  );
};
