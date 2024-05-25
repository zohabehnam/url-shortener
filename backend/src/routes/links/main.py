from fastapi import APIRouter, Body, Depends, HTTPException
from datetime import datetime, timezone

from fastapi.responses import RedirectResponse
from pydantic import HttpUrl
from sqlalchemy.orm import Session
from routes.links import models
from routes.links.controllers import create_short_link
from util.db_dependency import get_db


router = APIRouter(
    prefix="",
    tags=["links"],
    responses={404: {"description": "Not found"}},
)


@router.post("/api/shorten")
def get_short_link(
        db: Session = Depends(get_db), url: HttpUrl = Body(..., embed=True)
        ):
    if not url:
        raise HTTPException(status_code=400, detail="URL cannot be empty")
    timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    short_link = create_short_link(url, timestamp)
    obj = models.Link(original_url=url, short_link=short_link)
    db.add(obj)
    db.commit()
    return {"short_link": short_link}


@router.get("/{short_link}")
def redirect(short_link: str, db: Session = Depends(get_db)):
    obj = (
        db.query(models.Link)
        .filter_by(short_link=short_link)
        .order_by(models.Link.id.desc())
        .first()
    )
    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="The link does not exist, could not redirect."
        )
    print(obj.original_url)
    return RedirectResponse(url=obj.original_url)
