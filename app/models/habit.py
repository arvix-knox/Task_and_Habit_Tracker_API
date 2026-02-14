from __future__ import annotations

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Habit(Base):
    __tablename__ = "habits"
    __table_args__ = (
        sa.CheckConstraint(
            "frequency IN ('daily', 'weekly', 'monthly')",
            name="ck_habits_frequency",
        ),
    )

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(sa.Text, nullable=True)
    frequency: Mapped[str] = mapped_column(
        sa.String(20),
        nullable=False,
        server_default=sa.text("'daily'"),
    )
    target_count: Mapped[int] = mapped_column(
        sa.Integer,
        nullable=False,
        server_default=sa.text("1"),
    )
    created_at: Mapped[sa.DateTime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    updated_at: Mapped[sa.DateTime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("CURRENT_TIMESTAMP"),
    )


class HabitCompletion(Base):
    __tablename__ = "habit_completions"
    __table_args__ = (
        sa.UniqueConstraint(
            "habit_id",
            "completed_on",
            name="uq_habit_completions_habit_id_completed_on",
        ),
    )

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    habit_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        sa.ForeignKey("habits.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    completed_on: Mapped[sa.Date] = mapped_column(sa.Date, nullable=False)
    note: Mapped[str | None] = mapped_column(sa.Text, nullable=True)
    created_at: Mapped[sa.DateTime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("CURRENT_TIMESTAMP"),
    )
