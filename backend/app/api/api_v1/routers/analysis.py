#copy of users.py

from fastapi import APIRouter, Request, Depends, Response, encoders, BackgroundTasks
import typing as t
import requests

from app.db.session import get_db
from app.db.crud import (
    edit_post,
    get_post,
    get_sentiment_analysis,
    get_sentiment_analysis_by_post,
    create_sentiment_analysis
)
from app.db.schemas import PostEdit, SentimentAnalysisBase, SentimentAnalysisOut
from app.core.auth import get_current_active_user, get_current_active_superuser

analysis_router = r = APIRouter()

@r.get("/analysis/{sentiment_analysis_id}", response_model=SentimentAnalysisBase, response_model_exclude_none=True )
async def get_sentiment_by_id(
    sentiment_analysis_id: int,
    db=Depends(get_db)
):
    """
    Get sentiment analysis by id
    """
    return get_sentiment_analysis(db, sentiment_analysis_id)

@r.get("/analysis/post/{post_id}", response_model=SentimentAnalysisBase, response_model_exclude_none=True )
async def get_sentiment_by_post(
    post_id: int,
    db=Depends(get_db)
):
    """
    Get sentiment analysis by post
    """
    return get_sentiment_analysis_by_post(db, post_id)

@r.post("/analysis/{post_id}", response_model=SentimentAnalysisBase, response_model_exclude_none=True)
async def sentiment_analysis_create(
    post_id: int,
    db=Depends(get_db)
):
    """
    Create a new sentiment analysis
    """
    return create_sentiment_analysis(db, post_id)


