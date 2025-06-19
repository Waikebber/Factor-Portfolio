from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

class Tuner:
    """
    Universal hyperparameter tuner for all supported model types.
    Supports 'grid' or 'random' search.
    """
    def __init__(
        self,
        model_type: str,
        param_grid: dict,
        cv: int = 5,
        scoring: str = None,
        search_type: str = "grid",       # "grid" or "random"
        n_iter: int = 10,                # only for randomized
        random_state: int = 42,
        n_jobs: int = -1
    ):
        self.model_type   = model_type
        self.param_grid   = param_grid
        self.cv           = cv
        self.scoring      = scoring
        self.search_type  = search_type
        self.n_iter       = n_iter
        self.random_state = random_state
        self.n_jobs       = n_jobs
        self.searcher     = None

    def _make_base_estimator(self):
        """Instantiate an un-parameterized estimator of the right class."""
        if self.model_type == "linear":
            return LinearRegression()
        if self.model_type == "random_forest":
            return RandomForestRegressor(random_state=self.random_state)
        if self.model_type == "xgboost":
            return XGBRegressor(random_state=self.random_state)
        if self.model_type == "gbr":
            return GradientBoostingRegressor(random_state=self.random_state)
        raise ValueError(f"Unsupported model_type: {self.model_type}")

    def tune(self, X, y):
        """
        Run hyperparameter search. 
        Returns: (best_params, best_estimator_, cv_results_)
        """
        estimator = self._make_base_estimator()
        if self.search_type == "grid":
            self.searcher = GridSearchCV(
                estimator, self.param_grid,
                cv=self.cv,
                scoring=self.scoring,
                n_jobs=self.n_jobs,
                verbose=1
            )
        else:
            self.searcher = RandomizedSearchCV(
                estimator, self.param_grid,
                n_iter=self.n_iter,
                cv=self.cv,
                scoring=self.scoring,
                random_state=self.random_state,
                n_jobs=self.n_jobs,
                verbose=1
            )

        self.searcher.fit(X, y)
        return (
            self.searcher.best_params_,
            self.searcher.best_estimator_,
            self.searcher.cv_results_
        )
