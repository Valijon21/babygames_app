export type AgeBand = '2-4' | '5-7' | '8-10' | '11-14';

export interface GameCategory {
  id: number;
  slug: string;
  title: string;
  description: string;
  icon_key: string;
  sort_order: number;
}

export interface Game {
  id: number;
  slug: string;
  title: string;
  category_slug: string;
  category_title: string;
  min_age: number;
  max_age: number;
  difficulty: 'easy' | 'medium' | 'hard';
  difficulty_display: string;
  thumbnail: string;
  estimated_minutes: number;
  content_version: number;
}

export interface ChildProfile {
  id: string;
  display_name: string;
  age_band: AgeBand;
  avatar_key: string;
  preferences: {
    sound_enabled?: boolean;
    music_enabled?: boolean;
    reduced_motion?: boolean;
  };
}

export interface GameResult {
  score?: number;
  completed: boolean;
  duration_seconds: number;
  attempts?: number;
  stars?: number;
  result_summary?: Record<string, unknown>;
}
